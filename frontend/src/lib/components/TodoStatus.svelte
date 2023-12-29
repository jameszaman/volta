<!--
Copyright (c) 2023 James Hedayet Zaman
All rights reserved.
This code is the intellectual property of James Hedayet Zaman.
Unauthorized use, reproduction, or distribution is strictly prohibited.
For inquiries, please contact james.hedayet@gmail.com.
-->
<script>
    import Icon from '@iconify/svelte';
    import StatusSelector from './StatusSelector.svelte';

    export let status = undefined;
    export let todo_id = undefined;
    export let className = "";

    let isOpen = false;

    // Add here if you want to add any new type of status. Also need to add in StatusSelector.svelte
    let iconMap = {
        pending: { icon: 'ic:twotone-pending-actions', class: 'text-white' },
        progress: { icon: 'mdi:progress-clock', class: 'text-blue-400' },
        completed: { icon: 'carbon:checkmark-filled', class: 'text-green-500' },
        deferred: { icon: 'mdi:latest', class: 'text-orange-500' },
        canceled: { icon: 'material-symbols:cancel', class: 'text-red-500' },
        archived: { icon: 'ph:archive', class: 'text-purple-400' }
    };

    // Function to get the icon name based on the status
    function getIconName(status) {
        return iconMap[status]?.icon || 'pajamas:question'; // Default icon if status not found
    }

    function getIconClass(status) {
        return iconMap[status]?.class || 'text-red-500'; // Default icon if status not found
    }

    function toggleSelector() {
        isOpen = !isOpen;
    }
</script>

<div on:click={toggleSelector} on:keypress={toggleSelector} class="cursor-pointer relative group">
    <div class="absolute bottom-full left-1/2 transform -translate-x-1/2 text-xs rounded opacity-0 group-hover:opacity-100 transition duration-500">{status}</div>
    <Icon icon={getIconName(status)} class={`${className} ${getIconClass(status)} m-2 text-xl`} />
</div>
<StatusSelector bind:isOpen={isOpen} currentStatusName={getIconName(status)} todo_id={todo_id} bind:status={status} />