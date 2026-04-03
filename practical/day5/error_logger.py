def log_error(msg):
    with open('error.txt', 'a') as f:
        f.write(msg + '\n')


try:
    num = input('Enter a number: ')
    div = 10/num
except Exception as e:
    log_error('Invalid input:'+num)
    print("here")
