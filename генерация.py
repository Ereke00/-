from transformers import GPT2LMHeadModel, GPT2Tokenizer

# Загрузка предварительно обученной модели и токенизатора GPT-2
model_name = "gpt2"
tokenizer = GPT2Tokenizer.from_pretrained(model_name)
model = GPT2LMHeadModel.from_pretrained(model_name)

# Генерация текста
prompt_text = "Как поставить карьерные цели на год и реализовать их"
input_ids = tokenizer.encode(prompt_text, return_tensors='pt')

# Генерация следующих 100 токенов (слов)
output = model.generate(input_ids, max_length=100, num_return_sequences=1, temperature=0.7)

# Декодирование сгенерированного текста
generated_text = tokenizer.decode(output[0], skip_special_tokens=True)
print(generated_text)
