import gradio as gr

def binary_search(lst, target):
    steps = []  # store text output here
    
    low = 0
    high = len(lst) - 1
    step = 1
    steps.append(f"Target value is: {target}")

    while low <= high:
        mid = (low + high) // 2

        steps.append(f"Step {step}:")
        steps.append(f"  low = {low} (value = {lst[low]})")
        steps.append(f"  high = {high} (value = {lst[high]})")
        steps.append(f"  mid = {mid} (value = {lst[mid]})")

        if lst[mid] == target:
            steps.append(f"Target {target} found at index {mid}.")
            return "\n".join(steps)

        elif lst[mid] < target:
            steps.append(f"  {target} > {lst[mid]}, only searching right half now")
            low = mid + 1
        else:
            steps.append(f"  {target} < {lst[mid]}, only searching left half now")
            high = mid - 1

        step += 1

    steps.append(f"Target of {target} NOT found in the lst.")
    return "\n".join(steps)


def run_search(numbers_str, target_str): # converts the input text into a lst/target for the UI and returns binary search as string
    if not numbers_str.strip():
        return "Enter numbers."

    try:
        lst = [int(x.strip()) for x in numbers_str.split(",")]
        target = int(target_str.strip())
    except:
        return "Enter numbers only."

    return binary_search(lst, target)


app = gr.Interface(fn=run_search,
                   inputs=[gr.Textbox(label="Enter numbers, seperate them by commas.", placeholder="e.g. 1, 4, 7, 10"),
                           gr.Textbox(label="Enter target number", placeholder="e.g. 7")],
                   outputs=gr.Textbox(label="Search Steps"),
                   title="Binary Search",
                   description="Enter a list of integers and a target value you want to find within the list.")

if __name__ == "__main__": # if this file is the main program being run, start the app 
    app.launch()

