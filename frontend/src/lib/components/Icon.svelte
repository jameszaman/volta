<!--
Copyright (c) 2023 James Hedayet Zaman
All rights reserved.
This code is the intellectual property of James Hedayet Zaman.
Unauthorized use, reproduction, or distribution is strictly prohibited.
For inquiries, please contact james.hedayet@gmail.com.
-->
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
