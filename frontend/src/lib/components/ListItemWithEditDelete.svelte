<!--
Copyright (c) 2023 James Hedayet Zaman
All rights reserved.
This code is the intellectual property of James Hedayet Zaman.
Unauthorized use, reproduction, or distribution is strictly prohibited.
For inquiries, please contact james.hedayet@gmail.com.
-->
<!-- 
    * You must put id for using edit and delete function.
    * You must also follow the the proper function format.
 -->
<script>
    import Icon from "./Icon.svelte";
    import { toggleTaskItemDraggable } from "../../stores/todoStore.js";

    // Props
    // Functions
    export let deleteFunction = (id) => {}
    export let editFunction = (id, todo_update) => {}
    export let click = () => {}
    export let isLineThrough = false
    // props
    export let value = ""
    export let id = ""
    export let className = ""
    // Variables
    let isEditModalOpen = false
    let inputValue = value;

    // Whenever the value changes anywhere, update the inputValue global variable
    // If the next line seems confusing, then read up on Svelte's reactive declarations.
    $: inputValue = inputValue
    $: inputValue = value

    function toggleEditModal() {
        // Open or close the edit modal.
        isEditModalOpen = !isEditModalOpen
        // When we are editing, the user should not be able to drag any item.
        toggleTaskItemDraggable()
    }

    function editTodo(event) {
        // Close the model if the user presses escape
        if(event.key == "Escape") {
            toggleEditModal();
            return
        }
        // If the user presses enter, then update the todo
        if(event.key !== 'Enter') {
            return
        }
        // Do not update if the todo is empty
        if(inputValue !== "") {
            editFunction(id, inputValue);
        }
        // And also close the modal
        toggleEditModal();
    }
</script>

<li 
    class={className + " list-item m-2 list-none relative"}
    class:group={!isEditModalOpen}
    on:click={click}
    on:keypress={click}
>
    <span class="break-all group-hover:pr-10" class:hidden={isEditModalOpen} class:line-through={isLineThrough} >{value}</span>
    <div class:hidden={!isEditModalOpen}>
        <input type="text" bind:value={inputValue} class="w-full outline-none rounded bg-zinc-700 px-2" on:keyup={editTodo}>
        <Icon
            icon="carbon:close-filled"
            className="cursor-pointer hover:opacity-80 absolute right-2 top-1"
            actionFunction={() => toggleEditModal()}
        />
    </div>
    <div class="absolute right-0 top-0 flex" class:hidden={isEditModalOpen}>
        <!-- Edit Icon -->
        <Icon
            icon="iconamoon:edit-duotone"
            className="text-blue-300 group-hover:opacity-100 opacity-0 cursor-pointer text-2xl"
            actionFunction={() => toggleEditModal()}
        />
        <!-- Delete Icon -->
        <Icon
            icon="ic:baseline-delete"
            className="text-red-500 group-hover:opacity-100 opacity-0 cursor-pointer text-2xl"
            actionFunction={() => deleteFunction(id)}
        />
    </div>
</li>