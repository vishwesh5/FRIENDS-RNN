from textgenrnn import textgenrnn
textgen = textgenrnn()
textgen.train_from_file('0101.txt', num_epochs=10)
# print(textgen.generate(10, temperature=1.0))

