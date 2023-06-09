<script>
    let projectNames = ["Project 01", "Project 02", "Project 03", "Project 04"]
</script>

<nav>
    <div>
        Sidenav
    </div>
    <input type="text" class="searchbar" placeholder="Search For A Project">
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
        grid-row: 2/17;
    }

    .searchbar {
        padding: 0.2rem 0.3rem;
        margin: 0.5rem 1rem;
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
</style>