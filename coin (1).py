import amino
import getpass
import os
os.system("clear")
print("\033[1;36m Amino :  \033[1;34mSirLez \n \n \033[1;36minsta : \033[1;34m SirLe0x \n \n \n")
client=amino.Client()
ss=0
sz=25
nuum=0
tst=False
while tst==False:
	try:
		email=input("\033[1;31m\n# ur Email : \033[1;0m")
		password=getpass.getpass("\033[1;31m# ur Password : \033[1;0m")
		client.login(email=email,password=password)
		tst=True
	except:
		tst=False
		print("\n# Verify ur account! \n")
		exx=input("# continue? y/n : ")
		if exx=='N' or exx=='n' or exx=='no':
				os._exit(1)

tId=client.get_wallet_history(start=0,size=1).transanctionId

cht=input("\n\n\033[1;33m# Give Me The Chat url : \033[1;0m")
cht=client.get_from_code(cht)

comId=cht.path[1:cht.path.index("/")]
subclient=amino.SubClient(comId=comId,profile=client.profile)

cht=cht.objectId

print("\n\n\033[1;33mThe TransactionId : \033[1;0m"+tId.pop())

tran=input("\n\n\033[1;33mGive Me The TransactionId :\033[1;0m ")
while True:
	coins=input("\n\n\033[1;33mHow Much Coins ? :\033[1;0m ")

	subclient.send_coins(chatId=cht,coins=coins,transactionId=tran)

	print("\033[1;36mDone...")