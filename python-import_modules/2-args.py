
argm = ['NAME']
def args(argm):
    num_argm = len(argm)-1

    if num_argm == 0:
        print("0 arguments.")
    else:
        print(f"{num_argm} {'argument:' if num_argm == 1 else 'arguments:'}")

        counter = 1
        for elm in argm[1:]:
            print(f"{counter}: {elm}")
            counter += 1

# Example usage:
arguments_list = []
args(argm)
