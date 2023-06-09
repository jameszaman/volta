<script>
    import Todo from "../components/Todo.svelte";
</script>

<div class="main-div">
    <Todo />
</div>


<style>
    .main-div {
        grid-row: 2/17;
        grid-column: 3/13;
        display: grid;
        justify-items: center;
    }
</style>