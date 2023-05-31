import os
import tarfile
import numpy as np
import tensorflow as tf
from tensorflow.keras.preprocessing.text import Tokenizer
from tensorflow.keras.preprocessing.sequence import pad_sequences
import streamlit as st

# Step 1: Data Preparation
# Assume you have downloaded and extracted the SpamAssassin Public Corpus dataset.

# Path to the extracted dataset directory
dataset_dir = r'C:\Users\MSI GF63\OneDrive\Desktop\New fold\spamassassin'

# Read email files and labels
emails = []
labels = []
ham_dir = os.path.join(dataset_dir, 'easy_ham')
spam_dir = os.path.join(dataset_dir, 'spam')

# Read spam emails
for file_name in os.listdir(spam_dir):
    file_path = os.path.join(spam_dir, file_name)
    with open(file_path, 'r', encoding='latin1') as file:
        content = file.read()
        emails.append(content)
        labels.append(1)  # Spam label is 1

# Read non-spam (ham) emails
for file_name in os.listdir(ham_dir):
    file_path = os.path.join(ham_dir, file_name)
    with open(file_path, 'r', encoding='latin1') as file:
        content = file.read()
        emails.append(content)
        labels.append(0)  # Non-spam label is 0

# Shuffle the data
np.random.seed(42)
shuffle_indices = np.random.permutation(len(emails))
emails = np.array(emails)[shuffle_indices]
labels = np.array(labels)[shuffle_indices]

# Split the data into training and testing sets
train_size = int(0.8 * len(emails))
train_emails = emails[:train_size]
train_labels = labels[:train_size]
test_emails = emails[train_size:]
test_labels = labels[train_size:]

# Tokenize the email texts
tokenizer = Tokenizer()
tokenizer.fit_on_texts(train_emails)

vocab_size = len(tokenizer.word_index) + 1

# Convert text to sequences
train_sequences = tokenizer.texts_to_sequences(train_emails)
test_sequences = tokenizer.texts_to_sequences(test_emails)

# Pad sequences to have the same length
max_sequence_length = 1000  # Adjust as per your preference
train_data = pad_sequences(train_sequences, maxlen=max_sequence_length)
test_data = pad_sequences(test_sequences, maxlen=max_sequence_length)

# Step 2: Model Building
model = tf.keras.models.Sequential([
    tf.keras.layers.Embedding(vocab_size, 16, input_length=max_sequence_length),
    tf.keras.layers.GlobalAveragePooling1D(),
    tf.keras.layers.Dense(24, activation='relu'),
    tf.keras.layers.Dense(1, activation='sigmoid')
])

model.compile(loss='binary_crossentropy', optimizer='adam', metrics=['accuracy'])

# Step 3: Model Training
num_epochs = 10  # Adjust as per your preference
model.fit(train_data, train_labels, epochs=num_epochs, validation_data=(test_data, test_labels))

# Step 4: Model Evaluation
loss, accuracy = model.evaluate(test_data, test_labels)
st.write(f"Test Loss: {loss}")
st.write(f"Test Accuracy: {accuracy}")

# Step 5: Email Classification

# Function to preprocess and classify a given email
def classify_email(email_text):
    # Preprocess the email
    email_sequence = tokenizer.texts_to_sequences([email_text])
    email_data = pad_sequences(email_sequence, maxlen=max_sequence_length)
    
    # Classify the email
    prediction = model.predict(email_data)
    
    # Map the prediction to a label
    if prediction[0] >= 0.5:
        return "Spam"
    else:
        return "Non-Spam"

# Streamlit app
def main():
    st.title("Email Spam Classification")
    user_email = st.text_area("Enter the email text:", "")
    if st.button("Classify"):
        classification = classify_email(user_email)
        st.write(f"Email Classification: {classification}")

if __name__ == "__main__":
    main()
