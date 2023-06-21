<script>
    import Input from "../components/Input.svelte";

    let projectNames = ["Project 01", "Project 02", "Project 03", "Project 04"]
</script>

<nav>
    <div>
        Sidenav
    </div>
    <Input className="searchbar" placeholder="Search For A Project" />
    <ul>
        {#each projectNames as projectName}
            <li class="project-name">
                <a href="#{projectName}">{projectName}</a>
            </li>
        {/each}
        
    </ul>
</nav>

<style>
    nav {
        background-color: var(--dark4);
        display: flex;
        flex-direction: column;
        grid-column: 1/3;
    }

    .project-name {
        padding: 0.5rem;
    }

    a {
        text-decoration: none;
        color: var(--white);
    }

    a:hover {
        text-decoration: underline;
    }

    @media (max-width: 768px) {
        nav {
            grid-column: 1/13;
        }
    }
</style>