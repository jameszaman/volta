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
    export let editFunction = (id, todo_update) => {}
    export let click = () => {}
    // props
    export let value = ""
    export let id = ""
    export let className = ""
    // Variables
    let isEditModalOpen = false
    let todoValue = "";

    $: {
        todoValue = todoValue
    }

    function toggleEditModal() {
        isEditModalOpen = !isEditModalOpen
    }

    function editTodo(event) {
        if(event.key !== 'Enter') {
            return
        }
        editFunction(id, todoValue);
        toggleEditModal();
    }
</script>

<li 
    class={className + " list-item m-2 list-none relative group"}
    on:click={click}
    on:keypress={click}
>
    <span class="break-all" class:hidden={isEditModalOpen}>{value}</span>
    <input type="text" bind:value={todoValue} class:hidden={!isEditModalOpen} on:keypress={editTodo}>
    <!-- Edit Icon -->
    <span
        class="text-red-500 group-hover:opacity-100 opacity-0 cursor-pointer absolute right-6 text-2xl"
        on:click={() => toggleEditModal()}
        on:keypress={(event) => {
            if(event.key === 'Enter') {
                toggleEditModal()
            }
        }}
    >
        <Icon icon="line-md:edit-twotone"/>
    </span>
    <!-- Delete Icon -->
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