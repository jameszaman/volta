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

    // props
    export let current_project = 0

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

<nav>
    <div class="nav-top">
        <span>Project List</span>
        <button on:click={toggleButton}>
            <Icon icon={sideNavButtonIcon}/>
        </button>
    </div>
    <ProjectList className={projectListIsHidden} bind:projectNames={projectNames} bind:current_project={current_project}/>
    <CreateProject className={createProjectIsHidden} bind:projectNames={projectNames}/>
</nav>

<style>
    nav {
        background-color: var(--dark4);
        display: flex;
        flex-direction: column;
        grid-column: 1/4;
    }

    .nav-top {
        display: flex;
        justify-content: space-around;
        /* align-items: center; */
        font-size: 1.5rem;
    }
    .nav-top button {
        background-color: transparent;
        border: 0;
        cursor: pointer;
        color: white;
        font-size: 2rem;
    }

    @media (max-width: 768px) {
        nav {
            grid-column: 1/13;
        }
    }
</style>