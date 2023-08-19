use crate::entity::Entity;

struct Serum;

impl Serum {
    fn use_on(entity: &mut impl Entity) {
        entity.increase_health_by(10);
    }
}
