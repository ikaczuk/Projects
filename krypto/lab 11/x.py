num = '123456'
padded_num = num.zfill(64)
if padded_num is str:
    print(padded_num)
else:
    print("FAŁSZ")