<script>
    import Input from "./Input.svelte";
    import Button from "./Button.svelte";
    let list = [
        "Item #1",
        "Item #2",
        "Item #3",
        "Item #4",
        "Item #5",
        "Item #6",
    ]
</script>

<div class="todo">
    <form action="#">
        <Input />
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