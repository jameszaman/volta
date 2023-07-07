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
    class={className + " list-item"}
    on:click={click}
    on:keypress={click}
>
    <span>{value}</span>
    <span
        class="list-item-delete"
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

<style>
    .list-item {
        list-style: none;
        margin: 0.5rem;
        position: relative;
    }

    .list-item:hover .list-item-delete {
        opacity: 1;
    }

    .list-item-delete {
        opacity: 0;
        color: var(--red);
        cursor: pointer;
        position: absolute;
        right: 0;
        font-size: 1.5rem;
    }

    .project-name:hover {
        text-decoration: underline;
    }

    .project-name {
        padding: 0.5rem;
        cursor: pointer;
    }
</style>