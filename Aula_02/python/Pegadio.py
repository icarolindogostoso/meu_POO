L,D=map(int,input().split())
K,P=map(int,input().split())
pedagios=L//D
pagamento=L*K+pedagios*P
print(pagamento)