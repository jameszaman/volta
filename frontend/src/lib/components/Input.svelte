<script>
    // Props
    export let placeholder="";
    export let value="";
    export let className="";
</script>

<input type="text" {placeholder} bind:value={value} class={className}>

<style>
    input {
        padding: 0.2rem 0.3rem;
        font-size: 1rem;
    }

    .searchbar {
        padding: 0.2rem 0.3rem;
        margin: 0.5rem 1rem;
    }

    .margin0 {
        margin: 0;
    }
</style>