from jsonrpclib import Server

a = int(input("Enter a: "))
b = int(input("Enter b: "))

def main():
    conn = Server("http://localhost:1086")
    result = conn.get_multiplication(a,b)
    print(f"Result is: {result}")

if __name__ == "__main__":
    main()