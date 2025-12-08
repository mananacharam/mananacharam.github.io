<template>
  <div class="overview-section">
    <h2 class="section-title mb-4">Welcome to Mana Nacharam</h2>
    <p class="lead-text mb-5">
      Mana Nacharam is a vibrant village in Telangana, known for its rich cultural heritage, 
      agricultural traditions, and close-knit community.
    </p>

    <div class="stats-grid">
      <div class="stat-card stat-blue">
        <div class="stat-icon">
          <i class="fas fa-users"></i>
        </div>
        <div class="stat-value">2,500+</div>
        <div class="stat-label">Population</div>
      </div>

      <div class="stat-card stat-green">
        <div class="stat-icon">
          <i class="fas fa-seedling"></i>
        </div>
        <div class="stat-value">500+</div>
        <div class="stat-label">Acres Farmland</div>
      </div>

      <div class="stat-card stat-purple">
        <div class="stat-icon">
          <i class="fas fa-place-of-worship"></i>
        </div>
        <div class="stat-value">5</div>
        <div class="stat-label">Temples</div>
      </div>

      <div class="stat-card stat-orange">
        <div class="stat-icon">
          <i class="fas fa-vote-yea"></i>
        </div>
        <div class="stat-value">{{ totalVoters > 0 ? totalVoters.toLocaleString() : '1,800+' }}</div>
        <div class="stat-label">Registered Voters</div>
      </div>
    </div>
  </div>
</template>

<script>
export default {
  name: 'OverviewSection',
  props: {
    totalVoters: {
      type: Number,
      default: 0
    },
    totalWards: {
      type: Number,
      default: 0
    }
  }
}
</script>

<style scoped>
.overview-section {
  padding: 1rem 0;
}

.section-title {
  font-size: 2rem;
  font-weight: 700;
  color: var(--gray-900);
}

.lead-text {
  font-size: 1.125rem;
  color: var(--gray-700);
  line-height: 1.7;
}

.stats-grid {
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(200px, 1fr));
  gap: 1.5rem;
  margin-top: 2rem;
}

.stat-card {
  background: white;
  border-radius: var(--radius-md);
  padding: 2rem 1.5rem;
  text-align: center;
  box-shadow: var(--shadow-sm);
  transition: transform 0.2s, box-shadow 0.2s;
}

.stat-card:hover {
  transform: translateY(-4px);
  box-shadow: var(--shadow-md);
}

.stat-blue {
  background: linear-gradient(135deg, #eff6ff 0%, #dbeafe 100%);
  border-top: 4px solid #3b82f6;
}

.stat-green {
  background: linear-gradient(135deg, #f0fdf4 0%, #dcfce7 100%);
  border-top: 4px solid #10b981;
}

.stat-purple {
  background: linear-gradient(135deg, #faf5ff 0%, #f3e8ff 100%);
  border-top: 4px solid #a855f7;
}

.stat-orange {
  background: linear-gradient(135deg, #fff7ed 0%, #ffedd5 100%);
  border-top: 4px solid #f97316;
}

.stat-icon {
  font-size: 2.5rem;
  margin-bottom: 1rem;
}

.stat-blue .stat-icon {
  color: #3b82f6;
}

.stat-green .stat-icon {
  color: #10b981;
}

.stat-purple .stat-icon {
  color: #a855f7;
}

.stat-orange .stat-icon {
  color: #f97316;
}

.stat-value {
  font-size: 2rem;
  font-weight: 700;
  color: var(--gray-900);
  margin-bottom: 0.5rem;
}

.stat-label {
  font-size: 0.875rem;
  color: var(--gray-600);
  font-weight: 500;
}

@media (max-width: 768px) {
  .stats-grid {
    grid-template-columns: repeat(2, 1fr);
    gap: 1rem;
  }

  .stat-card {
    padding: 1.5rem 1rem;
  }

  .stat-value {
    font-size: 1.5rem;
  }

  .stat-icon {
    font-size: 2rem;
  }
}
</style>

