import gradio as gr
import random

def generate_array(size, max_value):
    try:
        size = int(size)
        max_value = int(max_value)
    except:
        return "❌ Please enter a valid integer ❌", [] #empty lists since our function is expecting an output with a list type for our grad.State

    if 1 > size or size > 10: #capping out at array lengths of 10
        return "❌ Please choose an array size between 1 and 10 ❌", []

    if max_value < 1:  #we define 0 as our floor below 
        return "❌ Please choose a maximum value of 1 or more ❌", []

    random_list = []
    for i in range(size): 
        random_list.append(random.randint(0, max_value))

    return str(random_list), random_list  #need the string version for Gradio display to user



def format_steps(arr):
    if not arr:
        return "❌ Please generate the array before sorting ❌", "", "" #expects 3 outputs

    arr_copy = arr.copy()
    steps = insertion_sort_steps(arr_copy)

    steps_formatted = []

    #adding the step numbers and alignment of |
    for i, step in enumerate(steps):
        #once the step number two digits we shorten the size to align with the single digits
        if i > 9: 
            row = f"{f'Step {i}':<8} | {step}"  #8 characters before the |
        else:
            row = f"{f'Step {i}':<9} | {step}"  #9 characters before the |
        steps_formatted.append(row)

    steps_output = "\n".join(steps_formatted) #new line between each step (to stack them)


    return str(arr), steps_output, str(arr_copy) #unsorted list, steps, sorted list




def insertion_sort_steps(arr):
    if not arr:
        return []

    steps = [f"✋   {arr.copy()}   |  {arr[0]} doesn't move (no elements to the left)"] #list to hold all of our steps (just copies)
    n = len(arr)
    i = 1

    while i < n:
        x = arr[i] #store our current value as "x"
        j = i - 1

        while j >= 0 and x < arr[j]:  #while our current element is smaller
            steps.append(f"⚖️   {arr.copy()}   |   Compare {x} with {arr[j]}") 
            #adding the 'comparison' step
            arr[j + 1] = arr[j]       #shift the larger element to the right
            steps.append(f"➡️   {arr.copy()}   |   Shift {arr[j]} to position {j + 1}") 
            #adding the 'shifting' step
            j -= 1

        arr[j + 1] = x                 #add one back since we took j one step too far left
        steps.append(f"🫳   {arr.copy()}   |   Place {x} at position {j + 1} ") 
        #adding the 'insertion' step
        i += 1

    return steps


#Gradio formatting
with gr.Blocks(title="Insertion Sort Demo") as demo:

    gr.Markdown("## 🧮 Insertion Sort Demo (Create your own array)")
    gr.Markdown("**Step 1:** Enter array size and max value → click *Generate Array*  \n"
                "**Step 2:** Click *Run Insertion Sort*")
    #Legend for our emojis
    with gr.Row():
        gr.Markdown("⚖️: Comparison between two elements") 
        gr.Markdown("➡️: Shifting elements to the right")
        gr.Markdown("🫳: Placing the element we \"picked up\"")
    

    arr_state = gr.State([]) #initializing for our array generation 

    with gr.Row():
        size_in = gr.Textbox(label="Array Size", placeholder="Enter list size...")
        max_in = gr.Textbox(label="Max Value", placeholder="Enter max value...")
        generate_btn = gr.Button("Generate Array")


    unsorted_box = gr.Textbox(label="Unsorted List")

    sort_btn = gr.Button("Run Insertion Sort")

    steps_box = gr.Textbox(label="Sorting Steps", lines=20)
    sorted_box = gr.Textbox(label="Sorted List")

    #Generate array
    generate_btn.click(
    fn=generate_array,
    inputs=[size_in, max_in],
    outputs=[unsorted_box, arr_state] #here we see where the two outputs go 
)


    #Insertion sort (running it while formatting the steps to show the user)
    sort_btn.click(
        fn=format_steps,
        inputs=arr_state,   #using the array we stored as the input
        outputs=[unsorted_box, steps_box, sorted_box]
    )

if __name__ == "__main__":
    demo.launch()
