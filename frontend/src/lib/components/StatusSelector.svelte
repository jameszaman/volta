<script>
    import Icon from '@iconify/svelte';

    export let className = "";
    export let isOpen = false;
    export let currentStatus = undefined;

    let allIcons = [
        { icon: 'ic:twotone-pending-actions', class: 'text-white' },
        { icon: 'mdi:progress-clock', class: 'text-green-300' },
        { icon: 'carbon:checkmark-filled', class: 'text-green-500' },
        { icon: 'mdi:latest', class: 'text-orange-500' },
        { icon: 'material-symbols:cancel', class: 'text-red-500' },
        { icon: 'ph:archive', class: 'text-green-500' }
    ]

    function selectStatus() {
        isOpen = !isOpen;
    }

</script>

<div class:icon-container-open={isOpen} class:icon-container-closed={!isOpen} on:click={selectStatus} on:keypress={selectStatus} class="flex justify-center outline-none rounded-xl absolute bg-gray-900 w-0 z-10">
    {#each allIcons as icon}
        <Icon
            icon={icon.icon}
            class={`${className} m-1 text-xl cursor-pointer hover:${icon.class} ${icon.icon === currentStatus ? icon.class : 'text-gray-400'}`}
        />
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
