from textgenrnn import textgenrnn
#textgen = textgenrnn(name="friends")
textgen = textgenrnn(weights_path='friends_weights.hdf5',
vocab_path='friends_vocab.json',
config_path='friends_config.json')
#textgen.reset()
textgen.train_from_largetext_file("mergedfile.txt",new_model=False,num_epochs=100,word_level=True,max_gen_length=50,max_words=5000,max_length=10)
generated_texts = textgen.generate(1,return_as_list=True)
with open("friends_out.txt",'w') as f:
	f.write(generated_texts)
