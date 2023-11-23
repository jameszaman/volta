<script>
    import TopNav from "./lib/layout/TopNav.svelte";
    import SideNav from "./lib/layout/SideNav.svelte";
    import Base from "./lib/layout/Base.svelte";
    import TailwindCss from "./TailwindCSS.svelte";

    let current_project = 0
</script>

<TailwindCss />

<main class="min-h-screen grid grid-rows-[6rem_auto] grid-cols-[20rem_auto]">
    <TopNav />
    <SideNav bind:current_project />
    <Base bind:current_project />
</main>
