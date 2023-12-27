<!--
Copyright (c) 2023 James Hedayet Zaman
All rights reserved.
This code is the intellectual property of James Hedayet Zaman.
Unauthorized use, reproduction, or distribution is strictly prohibited.
For inquiries, please contact james.hedayet@gmail.com.
-->
<script>
    import TopNav from "./lib/layout/TopNav.svelte";
    import SideNav from "./lib/layout/SideNav.svelte";
    import Base from "./lib/layout/Base.svelte";
    import TailwindCss from "./TailwindCSS.svelte";
</script>

<TailwindCss />

<main class="min-h-screen grid grid-rows-[4rem_auto] grid-cols-[20rem_auto]">
    <TopNav />
    <SideNav />
    <Base />
</main>
