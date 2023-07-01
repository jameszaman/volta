<script>
    // These are the components.
    import Input from "./Input.svelte";
    import Button from "./Button.svelte";
    import Icon from '@iconify/svelte'

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
            .then(todo_id => {
                // Also remove the todo from the frontend.
                list = list.filter(todo => {
                    console.log(todo.id, id, todo.id != id)
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
            <li class="todo">
                <span>{listItem.todo}</span>
                <span
                    class="todo-delete"
                    on:click={() => deleteTodo(listItem.id)}
                    on:keydown={(event) => {
                        if(event.key === 'Enter') {
                            deleteTodo(listItem.id)
                        }
                    }}
                >
                <Icon icon="ic:baseline-delete"/>
            </span>
            </li>
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

    .todo {
        list-style: none;
        margin: 0.5rem;
        position: relative;
    }
    .todo:hover .todo-delete {
        opacity: 1;
    }
    .todo-delete {
        opacity: 0;
        color: var(--red);
        cursor: pointer;
        position: absolute;
        right: 0;
        font-size: 1.5rem;
    }
</style>