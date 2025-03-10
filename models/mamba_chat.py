# import torch
# from transformers import MambaForCausalLM, AutoTokenizer
# from mamba_ssm.models.mixer_seq_simple import MambaLMHeadModel
#
# device = "cuda"
# tokenizer = AutoTokenizer.from_pretrained("havenhq/mamba-chat", local_files_only=True)
# tokenizer.eos_token = "<|endoftext|>"
# tokenizer.pad_token = tokenizer.eos_token
# tokenizer.chat_template = AutoTokenizer.from_pretrained("HuggingFaceH4/zephyr-7b-beta").chat_template
#
# model = MambaLMHeadModel.from_pretrained("havenhq/mamba-chat", device="cuda", dtype=torch.float16)
#
# messages = []
# while True:
#     user_message = input("\nYour message: ")
#     messages.append(dict(
#         role="user",
#         content=user_message
#     ))
#
#     input_ids = tokenizer.apply_chat_template(messages, return_tensors="pt", add_generation_prompt=True).to("cuda")
#
#     out = model.generate(input_ids=input_ids, max_length=2000, temperature=0.9, top_p=0.7, eos_token_id=tokenizer.eos_token_id)
#
#     decoded = tokenizer.batch_decode(out)
#     messages.append(dict(
#         role="assistant",
#         content=decoded[0].split("<|assistant|>\n")[-1])
#     )
#
#     print("Model:", decoded[0].split("<|assistant|>\n")[-1])




# from transformers import MambaForCausalLM, AutoTokenizer
#
# tokenizer = AutoTokenizer.from_pretrained("state-spaces/mamba-130m-hf")
# model = MambaForCausalLM.from_pretrained("state-spaces/mamba-130m-hf")
# input_ids = tokenizer("Hey how are you doing?", return_tensors="pt")["input_ids"]
#
# out = model.generate(input_ids, max_new_tokens=10)
# print(tokenizer.batch_decode(out))



from transformers import FalconMambaForCausalLM

