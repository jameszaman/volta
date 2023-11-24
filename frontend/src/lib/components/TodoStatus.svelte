<script>
    import Icon from '@iconify/svelte';

    export let status = undefined;
    export let className = "";

    let iconMap = {
        pending: { icon: 'ic:twotone-pending-actions', class: 'text-white' },
        progress: { icon: 'mdi:progress-clock', class: 'text-green-300' },
        completed: { icon: 'carbon:checkmark-filled', class: 'text-green-500' },
        deferred: { icon: 'mdi:latest', class: 'text-orange-500' },
        canceled: { icon: 'material-symbols:cancel', class: 'text-red-500' },
        archived: { icon: 'ph:archive', class: 'text-green-500' }
    };

    // Function to get the icon name based on the status
    function getIconName(status) {
        return iconMap[status]?.icon || 'pajamas:question'; // Default icon if status not found
    }

    function getIconClass(status) {
        return iconMap[status]?.class || 'text-red-500'; // Default icon if status not found
    }
</script>

<Icon icon={getIconName(status)} class={`${className} ${getIconClass(status)} mr-2 text-xl`} />
