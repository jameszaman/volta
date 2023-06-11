<script>
  
</script>

<nav>
    <div>
        This is the top Side Bar.
    </div>
    <input type="text" class="searchbar" placeholder="For Searching In The Whole Project">
    <div>
        <!-- Will hold dropdown in the future if needed. -->
    </div>
</nav>


<style>
    nav {
        display: flex;
        justify-content: space-between;
        align-items: center;
        background-color: var(--dark3);
        padding: 20px;
        border-bottom: 1px solid var(--dark);
        grid-column: 1/13;
    }

    .searchbar {
        padding: 0.5rem 0.75rem;
        width: 80%;
        font-size: 1.5rem;
    }
</style>