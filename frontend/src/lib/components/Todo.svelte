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

    // This is for tracking the input of todo.
    let inputValue = "";

    // We declare an empty array.
    let list = []

    // And fill the array with values from the database.
    fetch(`${import.meta.env.VITE_API_URL}/todo/all`)
    .then(res => res.json())
    .then(data => {
        list = [...data.map(todo => ({todo: todo.todo, id: todo._id}))]
    });

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
                    "todo": inputValue,
                })
            })
            .then(res => res.json())
            .then(todo_id => {
                // Also add the todo to the frontend.
                list = [...list, {"todo": inputValue, "id": todo_id}];
            })
        }
    }
    function deleteTodo(id) {
        // Make a DELETE request with necessary parameters to delete a todo.
        fetch(`${import.meta.env.VITE_API_URL}/todo/delete?id=${id}`, {
            method: "DELETE",
            headers: {
                "Content-Type": "application/json",
                "Accept": "*/*",
            }
        })
        .then(res => res.json())
        .then(data => {
            // Also remove the todo from the frontend.
            list = list.filter(todo => {
                return todo.id != id
            })
        })
    }
</script>


<div class="todo-container">
    <form on:submit|preventDefault={addToDo} action="#">
        <Input bind:value={inputValue} placeholder="New Todo"/>
        <Button> Submit </Button>
    </form>

    <ul>
        {#each list as listItem}
            <ListItemWithDelete deleteFunction={deleteTodo} value={listItem.todo} id={listItem.id}/>
        {/each}
    </ul>
</div>


<style>
    form {
        display: flex;
        gap: 1rem;
    }

    .todo-container {
        border: 1px solid var(--white);
        padding: 1rem;
        margin: 1rem;
        border-radius: 0.3rem;
    }
</style>