<template>
  <nav class="app-navigation">
    <div class="container-fluid">
      <ul class="nav-menu">
        <li>
          <a 
            href="#" 
            @click.prevent="$emit('navigate', 'about')" 
            :class="{ active: activeSection === 'about' }"
            class="nav-link"
          >
            <i class="fas fa-home"></i>
            <span>About</span>
          </a>
        </li>
        <li>
          <a 
            href="#" 
            @click.prevent="$emit('navigate', 'temples')" 
            :class="{ active: activeSection === 'temples' }"
            class="nav-link"
          >
            <i class="fas fa-place-of-worship"></i>
            <span>Temples</span>
          </a>
        </li>
        <li>
          <a 
            href="#" 
            @click.prevent="$emit('navigate', 'agriculture')" 
            :class="{ active: activeSection === 'agriculture' }"
            class="nav-link"
          >
            <i class="fas fa-seedling"></i>
            <span>Agriculture & Farming</span>
          </a>
        </li>
        <li>
          <a 
            href="#" 
            @click.prevent="$emit('navigate', 'facilities')" 
            :class="{ active: activeSection === 'facilities' }"
            class="nav-link"
          >
            <i class="fas fa-building"></i>
            <span>Village Facilities</span>
          </a>
        </li>
        <li>
          <a 
            href="#" 
            @click.prevent="$emit('navigate', 'voters')" 
            :class="{ active: activeSection === 'voters' }"
            class="nav-link"
          >
            <i class="fas fa-vote-yea"></i>
            <span>Voter Information</span>
          </a>
        </li>
      </ul>
    </div>
  </nav>
</template>

<script>
export default {
  name: 'AppNavigation',
  props: {
    activeSection: {
      type: String,
      default: 'about'
    }
  },
  emits: ['navigate']
}
</script>

<style scoped>
.app-navigation {
  background: white;
  border-bottom: 2px solid var(--gray-200);
  box-shadow: 0 2px 8px rgba(0, 0, 0, 0.05);
  position: sticky;
  top: 0;
  z-index: 1000;
}

.nav-menu {
  display: flex;
  list-style: none;
  padding: 0;
  margin: 0;
  gap: 0;
  justify-content: center;
  flex-wrap: wrap;
}

.nav-menu li {
  margin: 0;
}

.nav-link {
  display: flex;
  flex-direction: column;
  align-items: center;
  justify-content: center;
  padding: 1.25rem 1.5rem;
  color: var(--gray-700);
  text-decoration: none;
  transition: all 0.3s ease;
  font-weight: 500;
  font-size: 0.9375rem;
  border-bottom: 3px solid transparent;
  min-width: 120px;
  gap: 0.5rem;
}

.nav-link i {
  font-size: 1.25rem;
  color: var(--gray-600);
  transition: color 0.3s ease;
}

.nav-link span {
  white-space: nowrap;
}

.nav-link:hover {
  background: var(--gray-50);
  color: var(--primary);
  border-bottom-color: var(--primary-light);
}

.nav-link:hover i {
  color: var(--primary);
}

.nav-link.active {
  color: var(--primary);
  background: linear-gradient(to bottom, rgba(37, 99, 235, 0.05), transparent);
  border-bottom-color: var(--primary);
}

.nav-link.active i {
  color: var(--primary);
}

@media (max-width: 768px) {
  .nav-menu {
    overflow-x: auto;
    justify-content: flex-start;
    -webkit-overflow-scrolling: touch;
    scrollbar-width: none;
  }

  .nav-menu::-webkit-scrollbar {
    display: none;
  }

  .nav-link {
    min-width: 100px;
    padding: 1rem 1rem;
    font-size: 0.875rem;
  }

  .nav-link i {
    font-size: 1.125rem;
  }

  .nav-link span {
    font-size: 0.8125rem;
  }
}

@media (max-width: 640px) {
  .nav-link {
    min-width: 90px;
    padding: 0.875rem 0.75rem;
  }

  .nav-link span {
    font-size: 0.75rem;
  }
}
</style>

