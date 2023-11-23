<!--
Copyright (c) 2023 James Hedayet Zaman
All rights reserved.
This code is the intellectual property of James Hedayet Zaman.
Unauthorized use, reproduction, or distribution is strictly prohibited.
For inquiries, please contact james.hedayet@gmail.com.
-->
<script>
    import Icon from '@iconify/svelte'

    // Props
    // Functions
    export let deleteFunction = (id) => {}
    export let click = () => {}
    // Variables
    export let value = ""
    export let id = ""
    export let className = ""
</script>

<li 
    class={className + " list-item m-2 list-none relative group"}
    on:click={click}
    on:keypress={click}
>
    <span class=" break-all">{value}</span>
    <span
        class="text-red-500 group-hover:opacity-100 opacity-0 cursor-pointer absolute right-0 text-2xl"
        on:click={() => deleteFunction(id)}
        on:keypress={(event) => {
            if(event.key === 'Enter') {
                deleteFunction(id)
            }
        }}
    >
        <Icon icon="ic:baseline-delete"/>
    </span>
</li>