with open('emails_with_name.txt', 'r') as file_a, open('temp_mails_with_name.txt', 'r') as file_b:
    words_a = set(file_a.read().split())
    words_b = set(file_b.read().split())

unique_words = words_b.difference(words_a)

with open('emails_with_name.txt', 'a') as file_a:
    for word in unique_words:
        file_a.write(word + '\n')
