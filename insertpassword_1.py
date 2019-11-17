password = '12345'
i = 3
while i > 0:
	i = i-1
	psd = input('書いてください')
	if psd == password:
		print('密碼正確')
		break
	else:
		print('密碼錯誤')
		if i > 0:
			print('你還有', i, '機會')
		else:
			print('你沒有機會了')
			
