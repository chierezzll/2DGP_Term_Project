def collide(a, b):
    # fill here
    left_a, bottom_a, right_a, top_a = a.get_bb()
    left_b, bottom_b, right_b, top_b = b.get_bb()

    if left_a > right_b: return False
    if right_a < left_b: return False
    if top_a < bottom_b: return False
    if bottom_a > top_b: return False

    return True

def collide_2(a, b):
    # fill here
    left_a, bottom_a, right_a, top_a = a.get_bb_2()
    left_b, bottom_b, right_b, top_b = b.get_bb()

    if left_a > right_b: return False
    if right_a < left_b: return False
    if top_a < bottom_b: return False
    if bottom_a > top_b: return False

    return True

def collide_foot_head(a, b):
    # fill here
    left_a, bottom_a, right_a, top_a = a.get_bb_foot()
    left_b, bottom_b, right_b, top_b = b.get_bb_head()

    if left_a > right_b: return False
    if right_a < left_b: return False
    if top_a < bottom_b: return False
    if bottom_a > top_b: return False

    return True

def collide_head_foot(a, b):
    # fill here
    left_a, bottom_a, right_a, top_a = a.get_bb_head()
    left_b, bottom_b, right_b, top_b = b.get_bb_foot()

    if left_a > right_b: return False
    if right_a < left_b: return False
    if top_a < bottom_b: return False
    if bottom_a > top_b: return False

    return True

def collides_head_foot(b, a):
    # fill here
    left_a, bottom_a, right_a, top_a = a.get_bb_head()
    left_b, bottom_b, right_b, top_b = b.get_bb_foot()

    if left_a > right_b: return False
    if right_a < left_b: return False
    if top_a < bottom_b: return False
    if bottom_a > top_b: return False

    return True

def collide_item(a, b):
    # fill here
    left_a, bottom_a, right_a, top_a = a.get_bb_item()
    left_b, bottom_b, right_b, top_b = b.get_bb()

    if left_a > right_b: return False
    if right_a < left_b: return False
    if top_a < bottom_b: return False
    if bottom_a > top_b: return False

    return True