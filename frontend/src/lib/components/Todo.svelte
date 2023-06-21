<script>
    // These are the components.
    import Input from "./Input.svelte";
    import Button from "./Button.svelte";

    // We declare an empty array.
    let list = []

    // And fill the array with values from the database.
    fetch(`${import.meta.env.VITE_API_URL}/todo/all`)
    .then(res => res.json())
    .then(data => {
        list = [...data.map(todo => todo.todo)]
    });

    let inputValue = "";

    function addToDo() {
        if(inputValue) {
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
            list = [...list, inputValue];
        }
    }
</script>


<div class="todo">
    <form on:submit|preventDefault={addToDo} action="#">
        <Input bind:value={inputValue} placeholder="New Todo"/>
        <Button> Submit </Button>
    </form>

    <ul>
        {#each list as listItem}
            <li>{listItem}</li>
        {/each}
    </ul>
</div>


<style>
    form {
        display: flex;
        gap: 1rem;
    }

    .todo {
        border: 1px solid var(--white);
        padding: 1rem;
        margin: 1rem;
        border-radius: 0.3rem;
    }

    li {
        list-style: none;
        margin: 0.5rem;
    }
</style>