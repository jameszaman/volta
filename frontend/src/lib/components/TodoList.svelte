<!--
Copyright (c) 2023 James Hedayet Zaman
All rights reserved.
This code is the intellectual property of James Hedayet Zaman.
Unauthorized use, reproduction, or distribution is strictly prohibited.
For inquiries, please contact james.hedayet@gmail.com.
-->
<script>
    // These are the components.
    import Input from "./Input.svelte";
    import Button from "./Button.svelte";
    import ListItemWithDelete from "./ListItemWithDelete.svelte";
    import TodoStatus from "./TodoStatus.svelte";

    // props
    export let todoList = []
    export let current_project = 0

    // This is for tracking the input of todo.
    let inputValue = "";

    function addToDo() {
        if(inputValue) {
            // Make a POST request with necessary parameters to create a new todo.
            fetch(`${import.meta.env.VITE_API_URL}/todo/new?project_id=${current_project}`, {
                method: "POST",
                headers: {
                    "Content-Type": "application/json",
                    "Accept": "*/*",
                },
                body: JSON.stringify({
                    "todo": inputValue,
                })
            })
            .then(res => res.json())
            .then(new_todo => {
                // Also add the todo to the frontend.
                todoList = [...todoList, new_todo];
            })
        }
    }
    function deleteTodo(id) {
        // Make a DELETE request with necessary parameters to delete a todo.
        fetch(`${import.meta.env.VITE_API_URL}/todo/delete?id=${id}&project_id=${current_project}`, {
            method: "DELETE",
            headers: {
                "Content-Type": "application/json",
                "Accept": "*/*",
            }
        })
        .then(res => res.json())
        .then(data => {
            // Also remove the todo from the frontend.
            todoList = todoList.filter(todo => {
                return todo["_id"] != id
            })
        })
    }
</script>


<div class="border border-gray-400 p-4 m-4 rounded min-h-[50%] w-[90%] md:max-w-3xl flex flex-col items-center">
    <form on:submit|preventDefault={addToDo} action="#" class="flex w-full px-4">
        <Input bind:value={inputValue} placeholder="New Todo" className="rounded rounded-r-none outline-none w-full"/>
        <Button className=" text-sm py-0 rounded-l-none"> Submit </Button>
    </form>

    <ul class="w-full px-4 py-2">
        {#each todoList as listItem}
            <div class="flex items-center">
                <TodoStatus status={listItem.status} />
                <ListItemWithDelete deleteFunction={deleteTodo} value={listItem.todo} id={listItem["_id"]} className="w-full"/>
            </div>
        {/each}
    </ul>
</div>
