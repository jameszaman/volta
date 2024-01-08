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
    import TodoItem from "./TodoItem.svelte";

    // Assets
    import EmptyTaskList from "/assets/EmptyTaskList.svg";

    // props
    export let todoList = [];
    // prop functions
    export let dragOver = () => {};
    export let dragDrop = () => {};
    export let dragLeave = () => {};
    export let dragEnd = () => {};

    // Stores
    import { currentProject } from "../../stores/projectStore.js";
    import { currentlyDraggingTodoIndex } from "../../stores/todoStore";
  

    let current_project = ""
    currentProject.subscribe((value) => current_project = value);

    // This is for tracking the input of todo.
    let inputValue = "";

    function addToDo() {
        if(inputValue) {
            // Make a POST request with necessary parameters to create a new todo.
            fetch(`${import.meta.env.VITE_API_URL}/todo/new`, {
                method: "POST",
                headers: {
                    "Content-Type": "application/json",
                    "Accept": "*/*",
                },
                body: JSON.stringify({
                    "project_id": current_project,
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

    function editTodo(id, new_todo) {
        // Make a PATCH request with necessary body to update a todo.
        fetch(`${import.meta.env.VITE_API_URL}/todo/update_text`, {
            method: "PATCH",
            headers: {
                "Content-Type": "application/json",
                "Accept": "*/*",
            },
            body: JSON.stringify({
                "todo_id": id,
                "todo": new_todo,
                "project_id": current_project,
            })
        })
        .then(res => res.json())
        .then(updated_todo => {
            // Also update the todo from the frontend.
            todoList = todoList.map(todo => {
                if(todo["_id"] == id) {
                    todo["todo"] = updated_todo["todo"]
                }
                return todo
            })
        })
    }

    function dragstart_handler(event, index) {
        // Set the item that is being dragged.
        currentlyDraggingTodoIndex.set(index);
        // Set the drag's format and data.
        event.dataTransfer.setData("text/plain", event.target.id);
        event.dataTransfer.dropEffect = "move";
        // Remove the dragged item from
    }
</script>


<div
    class="border border-gray-400 p-4 m-4 rounded h-[85vh] w-[90%] md:max-w-3xl flex flex-col items-center bg-zinc-900 overflow-y-auto"
    on:dragover={dragOver}
    on:drop={dragDrop}
    on:dragleave={dragLeave}
    on:dragend={dragEnd}
    >
    <form on:submit|preventDefault={addToDo} action="#" class="flex w-full px-4">
        <Input bind:value={inputValue} placeholder="New Task" className="rounded rounded-r-none outline-none w-full"/>
        <Button className=" text-sm py-0 rounded-l-none"> Submit </Button>
    </form>

    {#if todoList.length}
        <ul class="w-full px-4 py-2">
            {#each todoList as listItem, index}
                <TodoItem
                    listItem={listItem}
                    editTodo={editTodo}
                    deleteTodo={deleteTodo}
                    dragStart={(e) => dragstart_handler(e, index)}
                />
            {/each}
        </ul>
    {:else}
        <div class="flex flex-col h-full justify-center items-center">
            <img src={EmptyTaskList} alt="Empty Task List" class="w-1/2"/>
            <p class="text-gray-200 text-center py-8 text-xl"> No remaining Task!🎉 </p>
        </div>
    {/if}
</div>
