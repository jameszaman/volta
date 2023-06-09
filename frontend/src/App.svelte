<script>
  import TopNav from "./lib/TopNav.svelte";
  import SideNav from "./lib/SideNav.svelte";
  import Base from "./lib/Base.svelte";
</script>

<main>
  <TopNav />
  <SideNav />
  <Base />
</main>

<style>
  main {
    min-height: 100vh;
    display: grid;
    grid-template-rows: repeat(16, 1fr);
    grid-template-columns: repeat(12, 1fr);
  }
</style>
