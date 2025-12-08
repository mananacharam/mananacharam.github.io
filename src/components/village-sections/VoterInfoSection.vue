<template>
  <div class="voter-info-section">
    <h2 class="section-title mb-4">
      <i class="fas fa-vote-yea me-2"></i>Voter Information
    </h2>

    <div v-if="!hasData" class="alert alert-info">
      <i class="fas fa-info-circle me-2"></i>
      No voter data available. Please check if the data file is loaded correctly.
    </div>

    <div v-else class="content-blocks">
      <div class="content-block block-orange">
        <h3 class="block-title">
          <i class="fas fa-chart-bar me-2"></i>Voter Statistics
        </h3>
        <div class="stats-grid">
          <div class="stat-box">
            <div class="stat-number">{{ totalVoters.toLocaleString() }}</div>
            <div class="stat-label">Total Registered Voters</div>
          </div>
          <div class="stat-box">
            <div class="stat-number stat-blue">{{ totalMale.toLocaleString() }}</div>
            <div class="stat-label">Male Voters</div>
          </div>
          <div class="stat-box">
            <div class="stat-number stat-pink">{{ totalFemale.toLocaleString() }}</div>
            <div class="stat-label">Female Voters</div>
          </div>
          <div class="stat-box">
            <div class="stat-number stat-green">{{ totalOthers.toLocaleString() }}</div>
            <div class="stat-label">Other Voters</div>
          </div>
        </div>
      </div>

      <div class="content-block block-blue">
        <h3 class="block-title">
          <i class="fas fa-poll me-2"></i>Polling Information
        </h3>
        <div class="info-list">
          <div class="info-item">
            <i class="fas fa-map-marker-alt me-2"></i>
            <div>
              <strong>Polling Station:</strong> Government High School, Mana Nacharam
            </div>
          </div>
          <div class="info-item">
            <i class="fas fa-landmark me-2"></i>
            <div>
              <strong>Assembly Constituency:</strong> Khammam
            </div>
          </div>
          <div class="info-item">
            <i class="fas fa-map me-2"></i>
            <div>
              <strong>Parliamentary Constituency:</strong> Khammam
            </div>
          </div>
          <div class="info-item">
            <i class="fas fa-chart-line me-2"></i>
            <div>
              <strong>Voter Turnout (Last Election):</strong> 87.3%
            </div>
          </div>
        </div>
      </div>

      <div class="content-block block-green">
        <h3 class="block-title">
          <i class="fas fa-clipboard-list me-2"></i>Voter Services
        </h3>
        <ul class="service-list">
          <li>
            <i class="fas fa-check-circle me-2"></i>
            <span>New voter registration available at Village Secretariat</span>
          </li>
          <li>
            <i class="fas fa-check-circle me-2"></i>
            <span>Voter ID card correction and updates</span>
          </li>
          <li>
            <i class="fas fa-check-circle me-2"></i>
            <span>Name in electoral roll verification</span>
          </li>
          <li>
            <i class="fas fa-check-circle me-2"></i>
            <span>Voter helpline: 1950 (Toll-free)</span>
          </li>
        </ul>
      </div>

      <div class="content-block block-purple">
        <h3 class="block-title">
          <i class="fas fa-users me-2"></i>Ward-wise Distribution
        </h3>
        <div class="ward-distribution">
          <div 
            v-for="(wardData, wardKey) in wardsData" 
            :key="wardKey"
            class="ward-item"
          >
            <div class="ward-info">
              <span class="ward-name">
                <i class="fas fa-map-pin me-2"></i>
                Ward {{ wardData.ward_no }}
              </span>
              <span class="ward-details">
                {{ wardData.mandal }} - {{ wardData.gram_panchayat }}
              </span>
            </div>
            <div class="ward-stats">
              <div class="ward-stat">
                <span class="ward-stat-label">Total:</span>
                <span class="ward-stat-value">{{ wardData.summary.total }}</span>
              </div>
              <div class="ward-stat">
                <span class="ward-stat-label">Male:</span>
                <span class="ward-stat-value stat-male">{{ wardData.summary.male }}</span>
              </div>
              <div class="ward-stat">
                <span class="ward-stat-label">Female:</span>
                <span class="ward-stat-value stat-female">{{ wardData.summary.female }}</span>
              </div>
            </div>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
import { computed } from 'vue'

export default {
  name: 'VoterInfoSection',
  props: {
    votersData: {
      type: Object,
      default: () => ({})
    },
    totalVoters: {
      type: Number,
      default: 0
    }
  },
  setup(props) {
    const totalMale = computed(() => {
      if (!props.votersData) return 0
      let total = 0
      for (const wardData of Object.values(props.votersData)) {
        total += wardData.summary.male
      }
      return total
    })

    const totalFemale = computed(() => {
      if (!props.votersData) return 0
      let total = 0
      for (const wardData of Object.values(props.votersData)) {
        total += wardData.summary.female
      }
      return total
    })

    const totalOthers = computed(() => {
      if (!props.votersData) return 0
      let total = 0
      for (const wardData of Object.values(props.votersData)) {
        total += wardData.summary.others || 0
      }
      return total
    })

    const wardsData = computed(() => {
      return props.votersData || {}
    })

    const hasData = computed(() => {
      return props.votersData && Object.keys(props.votersData).length > 0
    })

    return {
      totalMale,
      totalFemale,
      totalOthers,
      wardsData,
      hasData
    }
  }
}
</script>

<style scoped>
.voter-info-section {
  padding: 1rem 0;
  min-height: 400px;
}

.voter-info-section .alert {
  padding: 1.5rem;
  border-radius: var(--radius-md);
  margin-bottom: 2rem;
}

.section-title {
  font-size: 2rem;
  font-weight: 700;
  color: var(--gray-900);
}

.content-blocks {
  display: flex;
  flex-direction: column;
  gap: 1.5rem;
  margin-top: 2rem;
}

.content-block {
  padding: 2rem;
  border-radius: var(--radius-md);
  box-shadow: var(--shadow-sm);
}

.block-orange {
  background: linear-gradient(135deg, #fff7ed 0%, #ffedd5 100%);
}

.block-blue {
  background: linear-gradient(135deg, #eff6ff 0%, #dbeafe 100%);
}

.block-green {
  background: linear-gradient(135deg, #f0fdf4 0%, #dcfce7 100%);
}

.block-purple {
  background: linear-gradient(135deg, #faf5ff 0%, #f3e8ff 100%);
}

.block-title {
  font-size: 1.5rem;
  font-weight: 700;
  margin-bottom: 1.5rem;
  color: var(--gray-900);
}

.stats-grid {
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(200px, 1fr));
  gap: 1.5rem;
}

.stat-box {
  background: white;
  padding: 1.5rem;
  border-radius: var(--radius);
  text-align: center;
  box-shadow: var(--shadow-xs);
}

.stat-number {
  font-size: 2.5rem;
  font-weight: 700;
  color: #f97316;
  margin-bottom: 0.5rem;
}

.stat-number.stat-blue {
  color: #3b82f6;
}

.stat-number.stat-pink {
  color: #ec4899;
}

.stat-label {
  font-size: 0.875rem;
  color: var(--gray-600);
}

.info-list {
  display: flex;
  flex-direction: column;
  gap: 1rem;
}

.info-item {
  display: flex;
  align-items: flex-start;
  background: white;
  padding: 1rem;
  border-radius: var(--radius);
  box-shadow: var(--shadow-xs);
}

.info-item i {
  color: #3b82f6;
  margin-top: 0.125rem;
}

.service-list {
  list-style: none;
  padding: 0;
  margin: 0;
  display: flex;
  flex-direction: column;
  gap: 0.75rem;
}

.service-list li {
  display: flex;
  align-items: flex-start;
  background: white;
  padding: 1rem;
  border-radius: var(--radius);
  box-shadow: var(--shadow-xs);
}

.service-list i {
  color: #10b981;
  margin-top: 0.125rem;
}

.ward-distribution {
  display: flex;
  flex-direction: column;
  gap: 1rem;
}

.ward-item {
  background: white;
  padding: 1.5rem;
  border-radius: var(--radius);
  box-shadow: var(--shadow-xs);
  border-left: 4px solid #7c3aed;
}

.ward-info {
  display: flex;
  flex-direction: column;
  gap: 0.5rem;
  margin-bottom: 1rem;
}

.ward-name {
  font-size: 1.125rem;
  font-weight: 700;
  color: #7c3aed;
}

.ward-details {
  font-size: 0.875rem;
  color: var(--gray-600);
}

.ward-stats {
  display: flex;
  gap: 1.5rem;
  flex-wrap: wrap;
}

.ward-stat {
  display: flex;
  align-items: center;
  gap: 0.5rem;
}

.ward-stat-label {
  font-size: 0.875rem;
  color: var(--gray-600);
  font-weight: 500;
}

.ward-stat-value {
  font-size: 1rem;
  font-weight: 700;
  color: var(--gray-900);
}

.ward-stat-value.stat-male {
  color: #3b82f6;
}

.ward-stat-value.stat-female {
  color: #ec4899;
}

@media (max-width: 768px) {
  .content-block {
    padding: 1.5rem;
  }

  .stats-grid {
    grid-template-columns: 1fr;
  }

  .ward-stats {
    flex-direction: column;
    gap: 0.75rem;
  }
}
</style>

