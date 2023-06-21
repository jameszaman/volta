<script>
    import Todo from "../components/Todo.svelte";
</script>

<div class="main-div">
    <Todo />
</div>


<style>
    .main-div {
        grid-column: 3/13;
        display: grid;
        justify-items: center;
    }

    
    @media (max-width: 768px) {
        .main-div {
            grid-column: 1/13;
        }
    }
</style>