<!--
Copyright (c) 2023 James Hedayet Zaman
All rights reserved.
This code is the intellectual property of James Hedayet Zaman.
Unauthorized use, reproduction, or distribution is strictly prohibited.
For inquiries, please contact james.hedayet@gmail.com.
-->
<script>
    import Icon from "@iconify/svelte";
    import ProjectList from "../components/ProjectList.svelte";
    import CreateProject from "../components/CreateProject.svelte";

    // Declarations
    let projectNames = []

    // Variables for toggling between search and create project.
    let sideNavButtonIcon = 'mdi:create-new-folder-outline'
    let projectListIsHidden = ''
    let createProjectIsHidden = 'hidden'

    function toggleButton() {
        if(sideNavButtonIcon == 'mdi:create-new-folder-outline') {
            sideNavButtonIcon = 'gala:search'
            projectListIsHidden = 'hidden'
            createProjectIsHidden = ''
        }
        else {
            sideNavButtonIcon = 'mdi:create-new-folder-outline'
            projectListIsHidden = ''
            createProjectIsHidden = 'hidden'
        }
    }
</script>

<nav class="bg-zinc-900 flex flex-col col-span-12 p-4 md:col-span-1">
    <div class="flex justify-between text-2xl">
        <span>Project List</span>
        <button on:click={toggleButton} class="bg-transparent border-0 cursor-pointer text-white text-2xl">
            <Icon icon={sideNavButtonIcon}/>
        </button>
    </div>
    <ProjectList className={projectListIsHidden} bind:projectNames={projectNames} />
    <CreateProject className={createProjectIsHidden} bind:projectNames={projectNames}/>
</nav>
