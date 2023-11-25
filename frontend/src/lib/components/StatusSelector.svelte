<script>
    import Icon from '@iconify/svelte';

    // Stores
    import { currentProject } from "../../stores/projectStore.js";

    export let className = "";
    export let isOpen = false;
    export let currentStatusName = undefined;
    export let status = undefined;
    export let todo_id = undefined;

    let current_project = '';
    currentProject.subscribe((value) => current_project = value);

    // Add here if you want to add any new type of status. Also need to add in TodoStatus.svelte
    let allIcons = [
        { status: "pending", icon: 'ic:twotone-pending-actions', class: 'text-white' },
        { status: "progress", icon: 'mdi:progress-clock', class: 'text-blue-400' },
        { status: "completed", icon: 'carbon:checkmark-filled', class: 'text-green-500' },
        { status: "deferred", icon: 'mdi:latest', class: 'text-orange-500' },
        { status: "canceled", icon: 'material-symbols:cancel', class: 'text-red-500' },
        { status: "archived", icon: 'ph:archive', class: 'text-purple-400' }
    ]

    function selectStatus(newStatus) {
        // Only update if the status is different.
        if(status == newStatus) return;
        // Make a PATCH request with necessary parameters to update a todo.
        fetch(`${import.meta.env.VITE_API_URL}/todo/update_status?id=${todo_id}&project_id=${current_project}&status=${newStatus}`, {
            method: "PATCH",
            headers: {
                "Content-Type": "application/json",
                "Accept": "*/*",
            }
        })
        .then(res => res.json())
        .then(data => {
            // Now update the status in the Frontend.
            if(data.status === "success") {
                status = newStatus;
            }
        })
        .catch(err => console.error(err))
    }

    function statusSelectorToggle() {
        isOpen = false;
    }

</script>

<div on:click={statusSelectorToggle} on:keypress={statusSelectorToggle} class:icon-container-open={isOpen} class:icon-container-closed={!isOpen} class="flex justify-center outline-none rounded-xl absolute bg-gray-900 w-0 z-10 overflow-hidden left-2">
    {#each allIcons as icon}
        <span on:click={() => selectStatus(icon.status)} on:keypress={() => selectStatus(icon.status)}>
            <Icon
                icon={icon.icon}
                class={`${className} m-1 text-xl cursor-pointer hover:${icon.class} ${icon.icon === currentStatusName ? icon.class : 'text-gray-400'}`}
            />
        </span>
    {/each}
</div>

<style>
    .icon-container-open {
        width: 200px;
        transition: 0.5s ease-in;
    }
    .icon-container-closed {
        width: 0px;
        transition: 0.5s ease-in;
    }
</style>
