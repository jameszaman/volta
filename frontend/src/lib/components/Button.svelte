<script>

</script>

<button>
    <slot></slot>
</button>

<style>
    button {
        background-color: var(--primary);
        color: var(--blk);
        border: 0;
        font-size: 1.25rem;
        padding: 0.5rem 0.75rem;
        border-radius: 0.3rem;
    }
    button:hover {
        cursor: pointer;
    }
    
</style>
