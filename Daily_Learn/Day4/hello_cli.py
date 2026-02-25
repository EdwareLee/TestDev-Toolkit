import argparse

def say_hello(name: str, times: int):
    """打印问候语多次"""
    for i in range(times):
        print(f"[{i+1}] Hello, {name}!")

def main():
    parser = argparse.ArgumentParser(description="一个简单的问候工具")
    parser.add_argument("--name", required=True, help="要问候的人的名字")
    parser.add_argument("--times", type=int, default=1, help="问候次数（默认1次）")
    
    args = parser.parse_args()
    say_hello(args.name, args.times)

if __name__ == "__main__":
    main()