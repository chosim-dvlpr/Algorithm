function solution(skill, skill_trees) {
    let result = 0;
    skill_trees.forEach((tree) => {
        let newSkill = skill
        let flag = true
        for (let t of tree) {
            if (newSkill.length ===0 ) break
            if (newSkill.includes(t) && newSkill[0] === t) {
                newSkill = newSkill.slice(1,)
            } else if (newSkill.includes(t) && newSkill[0] !== t) {
                flag = false
                break
            }
        }
        if (flag) result++
    })
    
    return result
}
