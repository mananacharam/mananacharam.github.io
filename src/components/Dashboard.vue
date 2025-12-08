<template>
  <div class="dashboard">
    <div class="card">
      <div class="card-body">
        <div class="section-header mb-4">
          <h2 class="section-title">
            <i class="fas fa-chart-bar me-2 text-primary"></i>
            Voter Statistics Dashboard
          </h2>
          <p class="section-subtitle text-muted">
            Comprehensive overview of voter demographics and ward-wise distribution
          </p>
        </div>
        
        <div class="row g-3 g-md-4 mb-4">
          <div class="col-12 col-sm-6 col-md-6 col-lg-3">
            <div class="stat-card stat-card-male h-100">
              <div class="card-body position-relative">
                <div class="stat-card-bg">
                  <div class="circle circle-1"></div>
                  <div class="circle circle-2"></div>
                  <div class="circle circle-3"></div>
                </div>
                <div class="stat-content position-relative">
                  <div class="stat-icon mb-3">
                    <i class="fas fa-mars"></i>
                  </div>
                  <div class="stat-label mb-2">Male Voters</div>
                  <div class="stat-value">{{ totalStats.male.toLocaleString() }}</div>
                  <div class="stat-percentage">{{ malePercentage }}% of total</div>
                </div>
              </div>
            </div>
          </div>
          
          <div class="col-12 col-sm-6 col-md-6 col-lg-3">
            <div class="stat-card stat-card-female h-100">
              <div class="card-body position-relative">
                <div class="stat-card-bg">
                  <div class="circle circle-1"></div>
                  <div class="circle circle-2"></div>
                  <div class="circle circle-3"></div>
                </div>
                <div class="stat-content position-relative">
                  <div class="stat-icon mb-3">
                    <i class="fas fa-venus"></i>
                  </div>
                  <div class="stat-label mb-2">Female Voters</div>
                  <div class="stat-value">{{ totalStats.female.toLocaleString() }}</div>
                  <div class="stat-percentage">{{ femalePercentage }}% of total</div>
                </div>
              </div>
            </div>
          </div>
          
          <div class="col-12 col-sm-6 col-md-6 col-lg-3">
            <div class="stat-card stat-card-others h-100">
              <div class="card-body position-relative">
                <div class="stat-card-bg">
                  <div class="circle circle-1"></div>
                  <div class="circle circle-2"></div>
                  <div class="circle circle-3"></div>
                </div>
                <div class="stat-content position-relative">
                  <div class="stat-icon mb-3">
                    <i class="fas fa-transgender"></i>
                  </div>
                  <div class="stat-label mb-2">Other Voters</div>
                  <div class="stat-value">{{ totalStats.others.toLocaleString() }}</div>
                  <div class="stat-percentage">{{ othersPercentage }}% of total</div>
                </div>
              </div>
            </div>
          </div>
          
          <div class="col-12 col-sm-6 col-md-6 col-lg-3">
            <div class="stat-card stat-card-total h-100">
              <div class="card-body position-relative">
                <div class="stat-card-bg">
                  <div class="circle circle-1"></div>
                  <div class="circle circle-2"></div>
                  <div class="circle circle-3"></div>
                </div>
                <div class="stat-content position-relative">
                  <div class="stat-icon mb-3">
                    <i class="fas fa-users"></i>
                  </div>
                  <div class="stat-label mb-2">Total Voters</div>
                  <div class="stat-value">{{ totalStats.total.toLocaleString() }}</div>
                  <div class="stat-percentage">Across {{ totalWards }} wards</div>
                </div>
              </div>
            </div>
          </div>
        </div>

        <div class="ward-stats">
          <div class="d-flex justify-content-between align-items-center mb-3">
            <h3 class="mb-0" style="font-size: 1rem; font-weight: 600;">
              Ward-wise Statistics
            </h3>
            <small class="text-muted d-none d-md-block" style="font-size: 0.8125rem;">
              Click on a ward to view voters
            </small>
          </div>
          <div class="table-responsive">
            <table class="table table-hover table-striped align-middle table-sm">
              <thead class="table-dark">
                <tr>
                  <th class="d-none d-md-table-cell">
                    <i class="fas fa-map-marker-alt me-2"></i>
                    Ward
                  </th>
                  <th class="d-md-none">
                    <i class="fas fa-map-marker-alt"></i>
                  </th>
                  <th>
                    <i class="fas fa-mars text-primary d-none d-md-inline me-2"></i>
                    <span class="d-md-none"><i class="fas fa-mars text-primary"></i></span>
                    <span class="d-none d-md-inline">Male</span>
                  </th>
                  <th>
                    <i class="fas fa-venus text-danger d-none d-md-inline me-2"></i>
                    <span class="d-md-none"><i class="fas fa-venus text-danger"></i></span>
                    <span class="d-none d-md-inline">Female</span>
                  </th>
                  <th>
                    <i class="fas fa-transgender text-success d-none d-md-inline me-2"></i>
                    <span class="d-md-none"><i class="fas fa-transgender text-success"></i></span>
                    <span class="d-none d-md-inline">Others</span>
                  </th>
                  <th>
                    <i class="fas fa-users d-none d-md-inline me-2"></i>
                    <span class="d-md-none"><i class="fas fa-users"></i></span>
                    <span class="d-none d-md-inline">Total</span>
                  </th>
                  <th>
                    <i class="fas fa-percentage d-none d-md-inline me-2"></i>
                    <span class="d-md-none"><i class="fas fa-percentage"></i></span>
                    <span class="d-none d-md-inline">Percentage</span>
                  </th>
                </tr>
              </thead>
              <tbody>
                <tr 
                  v-for="ward in wardStats" 
                  :key="ward.wardKey"
                  @click="viewWardVoters(ward.wardKey)"
                  class="ward-row"
                >
                  <td>
                    <strong>
                      <i class="fas fa-map-pin text-primary me-2"></i>
                      {{ ward.wardNo }}
                      <i class="fas fa-chevron-right text-muted ms-2 small"></i>
                    </strong>
                  </td>
                  <td>
                    <span class="badge bg-primary">{{ ward.male }}</span>
                  </td>
                  <td>
                    <span class="badge bg-danger">{{ ward.female }}</span>
                  </td>
                  <td>
                    <span class="badge bg-success">{{ ward.others }}</span>
                  </td>
                  <td>
                    <strong class="text-primary">{{ ward.total }}</strong>
                  </td>
                  <td>
                    <span class="badge bg-secondary">{{ ward.percentage }}%</span>
                  </td>
                </tr>
              </tbody>
            </table>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
import { computed } from 'vue'

export default {
  name: 'Dashboard',
  props: {
    votersData: {
      type: Object,
      required: true
    }
  },
  emits: ['view-ward'],
  setup(props, { emit }) {
    const viewWardVoters = (wardKey) => {
      emit('view-ward', wardKey)
    }

    const totalStats = computed(() => {
      let male = 0
      let female = 0
      let others = 0
      let total = 0

      for (const wardData of Object.values(props.votersData)) {
        male += wardData.summary.male
        female += wardData.summary.female
        others += wardData.summary.others
        total += wardData.summary.total
      }

      return { male, female, others, total }
    })

    const totalWards = computed(() => {
      return Object.keys(props.votersData).length
    })

    const malePercentage = computed(() => {
      if (totalStats.value.total === 0) return 0
      return ((totalStats.value.male / totalStats.value.total) * 100).toFixed(1)
    })

    const femalePercentage = computed(() => {
      if (totalStats.value.total === 0) return 0
      return ((totalStats.value.female / totalStats.value.total) * 100).toFixed(1)
    })

    const othersPercentage = computed(() => {
      if (totalStats.value.total === 0) return 0
      return ((totalStats.value.others / totalStats.value.total) * 100).toFixed(1)
    })

    const wardStats = computed(() => {
      const wards = []
      const total = totalStats.value.total

      for (const [wardKey, wardData] of Object.entries(props.votersData)) {
        const percentage = total > 0 
          ? ((wardData.summary.total / total) * 100).toFixed(1)
          : '0.0'
        
        wards.push({
          wardKey,
          wardNo: wardData.ward_no,
          male: wardData.summary.male,
          female: wardData.summary.female,
          others: wardData.summary.others,
          total: wardData.summary.total,
          percentage
        })
      }

      // Sort by ward number
      return wards.sort((a, b) => {
        const numA = parseInt(a.wardNo.match(/\d+/)?.[0] || '0')
        const numB = parseInt(b.wardNo.match(/\d+/)?.[0] || '0')
        return numA - numB
      })
    })

    return {
      totalStats,
      totalWards,
      malePercentage,
      femalePercentage,
      othersPercentage,
      wardStats,
      viewWardVoters
    }
  }
}
</script>
