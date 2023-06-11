<script>
    export let placeholder="";
    export let value="";
</script>

<input type="text" {placeholder} bind:value={value}>

<style>
    input {
        padding: 0.2rem 0.3rem;
        font-size: 1rem;
    }
</style>