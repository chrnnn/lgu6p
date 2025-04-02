class BankAccount:
    def __init__(self, owner, pw, balance=0):
        self.owner = owner
        self.pw = pw
        self.balance = balance
        print(f"{owner}님의 계좌가 잔액 {balance}원으로 개설되었습니다.")

    # 입금
    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            print(f"{amount}원이 입금되었습니다.")
        else:
            print("0보다 큰 금액을 입금해 주세요.")

    # 출금
    def withdraw(self, amount):
        if self.balance >= amount >0:
            self.balance -= amount
            print(f"{amount}원이 출금되었습니다.")
        else:
            print("잔액보다 더 많은 금액을 출금할 수 없습니다")
        
    # 남은 잔고 출력
    def get_balance(self):
        input_pw = input("비밀번호를 입력해 주세요: ")
        if input_pw == self.pw:
            print(f"계좌의 현재 잔액은 {self.balance}원입니다.")
        else:
            print("비밀번호가 틀렸습니다.")

    # 송금
    def remittance(self, amount, account):
        # amount만큼 금액 차감
        account2.withdraw(amount)
        # amount만큼 acount에 입금
        account.deposit(amount)


account1 = BankAccount("홍길동", "1234", 10000)
account1.deposit(5000)
account1.withdraw(15000)
account1.get_balance()

account2 = BankAccount("김길동", "0000", 1000000)
account2.get_balance()

account2.remittance(50000, account1)
account1.get_balance()