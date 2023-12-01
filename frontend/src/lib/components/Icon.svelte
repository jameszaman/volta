<script>
    import Icon from '@iconify/svelte'

    export let icon = "iconamoon:edit-duotone"
    export let className = ""

    export let actionFunction = () => {}
</script>


<span
    class={className}
    on:click={() => actionFunction()}
    on:keypress={(event) => {
        if(event.key === 'Enter') {
            actionFunction()
        }
    }}
>
    <Icon icon={icon}/>
</span>
